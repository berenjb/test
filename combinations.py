import itertools
import cPickle as pickle


Flights = {}

with open("./ds_hash_ekpn.csv2", "r") as fin:
    fin.next()
    for record in fin:
        record = record.strip().split(",")
        if not Flights.has_key(record[1]):
            Flights[record[1]] = []
        Flights[record[1]].append( record[0] )

       
# most common pairs ...
print "Processing: Pairs ..."

Pairs = {}
for x in Flights:
    for p in itertools.combinations(sorted(set(Flights[x])), 2):
        if not Pairs.has_key(p[0] + ":" + p[1]):
            Pairs[p[0] + ":" + p[1]] = 0
        Pairs[p[0] + ":" + p[1]] += 1

print "  Done, saving ..."
pickle.dump(Pairs, open("./Pairs.p", "w" ))


# influencers
print "Processing: Influencers ..."

Influencers = {}

for x in Pairs:
    for p in x.split(":"):
        if not Influencers.has_key(p):
            Influencers[p] = 0
        Influencers[p] += 1

print "  Done, saving ..."
pickle.dump(Influencers, open("./Influencers.p", "w" ))


#
print
print
print "# Flights:", len(Flights)
print "# Pairs:", len(Pairs)
print 
print "-- Top 100 Pairs:"

for x in sorted(Pairs, key=Pairs.get, reverse=True)[:100]:
    p = x.split(":")
    
    print p[0], p[1], Pairs[x]

print
print "-- Top 100 Influencers:"

for x in sorted(Influencers, key=Influencers.get, reverse=True)[:100]:
    print x, Influencers[x]

print


