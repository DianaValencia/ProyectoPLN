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

java -mx700m -cp "$scriptdir/stanford-ner.jar:" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/classifiers/english.all.3class.distsim.crf.ser.gz -textFile $1
