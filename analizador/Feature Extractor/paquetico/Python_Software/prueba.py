from nltk.corpus import stopwords

stop = stopwords.words('english')
stopi = set(stop)
#print stop

#if "aRE".lower() in stop:
#    print "Found it!"

go = set(["are", "my"])
crisis = stopi - go

#print crisis
if "aRE".lower() not in crisis:
    print "exito"

#crisis.update(["YOLO", "WAKALAKA", 123]) Asi es como se agrega
crisis1 = list(crisis)
if "aRE".lower() in stop:
    print "auch"

if "thEy".lower() in stopi:
    print "auch auch"
#print len(stop)
#crisis1.sort
#print crisis1
