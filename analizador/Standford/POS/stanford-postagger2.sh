#!/bin/sh
#
# usage: ./stanford-postagger.sh model textFile
#  e.g., ./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt


if [ ! $# -ge 1 ]; then
  echo Usage: `basename $0` 'file(s)'
  echo
  exit
fi

scriptdir=`dirname $0`

java -mx300m -cp "$scriptdir/*:" edu.stanford.nlp.tagger.maxent.MaxentTagger -model $1 -textFile $2
