from random import randint

def geohash_lookup(zipcodeA, zipcodeB):
  pass

def geo_query(zipcode_a, zipcode_b):
  # Just an example response from :
  return randint(5, 60)


provider_zipcodes = ['10001', '10002', '10005', '10001', '10001', '12345']
booking_zipcodes = ['10001', '10002', '10005', '12312', '17012', '11212', '10036' '10001', '12345']

lookup_hash = {}

for provider_zip in provider_zipcodes:
  for booking_zip in booking_zipcodes:
    hashkey = frozenset((provider_zip, booking_zip))
    if hashkey in lookup_hash:
      print "Cache HIT: " + str(list(hashkey)) + " Already calculated as: " + str(lookup_hash[hashkey])
    else:
      lookup_hash[hashkey] = geo_query(provider_zip, booking_zip)
      print "Cache MISS: " + str(list(hashkey)) + " => " + str(lookup_hash[hashkey])

