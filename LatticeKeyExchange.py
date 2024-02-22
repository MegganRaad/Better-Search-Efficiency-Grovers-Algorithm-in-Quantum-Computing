From latticecrypto import LWEKeyExchange 

#LWE key exchange param
lweParams = {
     'n': 512,
     'q': 4093,
     'std_dev': 3.2
}

#initialize key exchange objects
Ember = LWEKeyExchange(lweParams)
Daniel = LWEKeyExchange(lweParams)

#Embers public and private keys
Ember_public_key, Ember_private_key = Ember.generate_keypair()
#Daniels public and private keys
Daniel_public_key, Daniel_private_key = Daniel.generate_keypair()
Ember_shared_secret = Ember.generate_shared_secret(Daniel_public_key,
Ember_private_key)

Daniel_shared_secret =
Daniel.generate_shared_secret(Ember_public_key, Daniel_private_key)

#checking shared secrets are the same
Assert Ember_shared_secret == Daniel_shared_secret
print("Shared secret has been established successfully")