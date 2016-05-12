#!/bin/perl 

#***************************************************************************************************
# 		SENTENCE SPLITTER

# Author:	Paul Clough 	{cloughie@dcs.shef.ac.uk}

# Description:	This sentence splitter is a very simple splitter that acts as a 
#		base-line to evaluate further splitters. The simple rule is this:

#		All [.!?] are considered as a sentence terminal if followed 
#		by at least one whitespace and a capital letter (also allow
#		for optional brackets and quotes).

#		$sentence_break = /[.!?][ ()"]+[A-Z]

# Input:	An ASCII text file e.g. blob.txt

# Output:	The input ASCII text file but with one sentence per line
#		and all [.!?] marked with category [sentence_break] or
# 		[non_sentence_break]. The output filename is the input
#		filename appended with ".split".

# Known bugs:	The program ignores anything after the last sentence of the input stream. 
#		This means that some text from the splitter at the end of the file could
#		appear missing. This has not been a problem to date, but may appear as a 
#		problem in the future. A further release of splitter will resolve this.

# Uses:		The program makes use of two files: 1) splitter.dict - a simple lexicon and
#		2) splitter.abv - a list of abbreviation exceptions that do not match the 
#		simple abbreviation detection rules.

# Useage:	%perl splitter.pl -f <file to split> -o

#		e.g. %perl splitter.pl [-f input.txt] -o

#		This outputs the split text to a file named input.txt.split

#		No -f option invokes input from STDIN

#		No -o option prints split text to STDOUT

# Revision:	30/03/01	Version 1.0

#		Any problems or suggestions for improvements, please email me.

#***************************************************************************************************

require 5.004;
require "getopts.pl";

&Getopts('f:o');

$dictionary = "argumentos.dict";
$abbrv_file = "splitter.abv";
$len = 0;
@COMMON_TERMS = ();
@ABBREVIATIONS = ();
$output_file = "salida.split";
#$output_file = "$opt_f.split";

if ($opt_o) {
	open(OUTPUT_FILE, ">$output_file") || die "cannot create the output file: $!";
	print OUTPUT_FILE "\n";
} else {
	print STDOUT "\n";
}

# Load in the dictionary and find the common words.
# Here, we assume the words in upper case are simply names and one
# word per line - i.e. in same form as /usr/dict/words
&loadDictionary;

# Same assumptions as for dictionary
&loadAbbreviations;

if ($opt_f) {
	open(FILE, $opt_f) or die "Can't open $opt_f for reading\n";

	while (defined ($line = <FILE>)) {
		$text.= $line;
	}
	close(FILE);
} else {
 	# get input from stdin	
 	while (defined ($line = <STDIN>)) {
		$text.= $line;
	}
}

# Remove any carriage returns etc.
$text =~ tr/\n\r/ /;

# for my purposes, remove hex 19 (^Y character)
$text =~ tr/\x19//d;

# make sure there are always spaces following punctuation to enable splitter to work 
# properly - covers such cases as believe.I ... where a space has forgotten to be 
# inserted.
$text =~ s/(.*)([.!?])(.*)/$1$2 $3/g;
$text.="\n";

# sentence ends with [.!?], followed by capital or number. Use base-line splitter and then
# use some heuristics to improve upon this e.g. dealing with Mr. and etc. 
# In this rather large regex we allow for quotes, brackets etc. 
# $1 = the complete sentence including beginning punctuation and brackets
# $2 = the punctuation mark - either [.!?:]
# $3 = the brackets or quotes after the [!?.:]. This is non-grouping i.e. does not consume.
# $4 = the next word after the [.?!:].This is non-grouping i.e. does not consume.
# $5 = rather than a next word, it may have been the last sentence in the file. Therefore capture
#      punctuation and brackets before end of file. This is non-grouping i.e. does not consume.
while ($text =~ /([\'\"`]*[({[]?[a-zA-Z0-9]+.*?)([\.!?:])(?:(?=([([{\"\'`)}\]<]*[ ]+)[([{\"\'`)}\] ]*([A-Z0-9][a-z]*))|(?=([()\"\'`)}\<\] ]+)\s))/gs ) {
	
	$sentence = $1;
	$punctuation = $2;
	if (defined($3)) { 
		$stuff_after_period = $3; 
	} else { 
		if ($5) { 
			$stuff_after_period = $5; 
		} else { 
			$stuff_after_period = ""; 
		}
	}
		
	@words = split(/\s+/, $sentence);
	$len+=@words;
	
	if ($4) { $next_word = $4; } else { $next_word = ""; }
	
	if ($punctuation =~ /[\.]/) {
		# consider the word before the period => is it an abbreviation? (then not full-stop)
		# Abbreviation if:
		#  1) all consonants and not all capitalised (and contain no lower case y e.g. shy, sly
		#  2) a span of single letters followed by periods
		#  3) a single letter (except I).
		#  4) in the known abbreviations list.
		# In above cases, then the period is NOT a full stop.
		
		# perhaps only one word e.g. P.S rather than a whole sentence
		$sentence =~ /\s+([a-zA-Z\.]+)$|([a-zA-Z\.]+)$/;
		
		if ($1) { $last_word = $1; } else { $last_word = $2; }
		
		if ( (($last_word !~ /.*[AEIOUaeiou]+.*/)&&($last_word =~ /.*[a-z]+.*/)&&($last_word !~ /.*[y]+.*/))|| 
		     ($last_word =~ /([a-zA-Z][\.])+/)||
		     (($last_word =~ /^[A-Za-z]$/)&&($last_word !~ /^[I]$/))||
		     ($abbreviation =~ / $last_word /i) ) { 		

			# We have an abbreviation, but this could come at the middle or end of a 
			# sentence. Therefore we assume that the abbreviation is not at the end of 
			# a sentence if the next word is a common word and the abbreviation occurs
			# less than 5 words from the start of the sentence.		     	
		     	
			$next_word = lc $next_word;
			 
			if ( ($common_term =~ / $next_word /)&&($len > 6) ) {
				# a sentence break
			        &print_sentence("$sentence"."$punctuation"."[sentence_break]"."$stuff_after_period");
				$len = 0;
			
			} else {
		     		# not a sentence break
				&print_non_sentence("$sentence"."$punctuation"."[non_sentence_break] ");
			}
		} else {
			# a sentence break
			&print_sentence("$sentence"."$punctuation"."[sentence_break]"."$stuff_after_period");
			$len = 0;
		}
		
	} else {
	 	# only consider sentences if : comes after at least 6 words from start of 
	  	# sentence
	  	if (($punctuation =~ /[!?]/)||(($punctuation =~ /[:]/)&&($len > 6))) {
	    		# a sentence break	
	    		&print_sentence("$sentence"."$punctuation"."[sentence_break]"."$stuff_after_period");
	    		$len = 0;
	  	} else {
	    		# not a sentence break
	    		&print_non_sentence("$sentence"."$punctuation"."[non_sentence_break] ");
	  	}
	}
}

if ($opt_o) { 
  close(OUTPUT_FILE);
}

exit;

#***************************************************************************************************

#***************************************************************************************************
# procedures
#***************************************************************************************************

sub loadDictionary {

	# Initialise var
	$common_term = "";	

	if (open(DICT, $dictionary)) {

		while (defined ($line = <DICT>)) {
			chomp($line);
			if ($line !~ /^[A-Z]/) {
				push(@COMMON_TERMS, "$line");	
			}
	
		}		
		
		close(DICT);
		
		# build up the common word list
		foreach $word (@COMMON_TERMS) {
			$common_term .= $word.' ';
		}
		chop $common_term;
	} else {
		print "cannot open dictionary file $opt_d: $!";		
	}
}

sub loadAbbreviations {

	# Initialise var
	$abbrv_term = "";	

	if (open(ABBRV, $abbrv_file)) {

		while (defined ($line = <ABBRV>)) {
			chomp($line);
			push(@ABBREVIATIONS, "$line");	
		}		
		
		close(ABBRV);
	
		# build up the abbreviations list
		foreach $word (@ABBREVIATIONS) {
			$abbreviation .= $word.' ';
		}
		chop $abbreviation;
	} else {
		print "cannot open dictionary file $opt_d: $!";		
	}
}

sub print_sentence {

  my $sentence = shift;
  my $final_sentence = "";
  
  # deal with anything after the [.!?:][sentence_break] and add this to the end e.g. "  
  $sentence =~ /\[sentence_break\](.*)$/;
  $leftover = $1;
  
  while ($sentence =~ /(.*?)([\.!?:])/gs) {
    $final_sentence.= $1.$2."[non_sentence_break]";
  }  
  
  $final_sentence =~ s/\[non_sentence_break\]$/[sentence_break]/;
  $final_sentence.=$leftover;
  
  # added these to allow \n as a sentence break tag and remove non_sentence_break tags
  $final_sentence =~ s/\[non_sentence_break\]//g;
  $final_sentence =~ s/\[sentence_break\](.*)/$1\n/;
 
  if ($opt_o) { 
  	print OUTPUT_FILE "$final_sentence\n\n";
  } else {
  	print STDOUT "$final_sentence\n\n";
  }
}

sub print_non_sentence{

  my $sentence = shift;
  my $final_sentence = "";

  while ($sentence =~ /(.*?)([\.!?:])/gs) {
    #$final_sentence.= $1.$2."[non_sentence_break]";
    $final_sentence.= $1.$2;
  }  

  $final_sentence =~ s/\[non_sentence_break\]//g;
  
  if ($opt_o) { 
  	print OUTPUT_FILE "$final_sentence ";
  } else {
  	print STDOUT "$final_sentence ";
  }	
}

#***************************************************************************************************
