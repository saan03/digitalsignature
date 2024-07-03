Digital Signature

Overview 
Digital signatures are cryptographic tools used to validate the authenticity and integrity of a message, software, or digital document. It serves as a digital equivalent of a handwritten signature or a stamped seal, but it offers far more inherent security.

Digital Signature Verification
A sender first generates a key pair: a private key kept confidential and a public key shared widely. When signing a document, the sender uses their private key to create a unique signature. This process involves hashing the document to generate a fixed-size string of bytes, which is then encrypted using the private key. The resulting digital signature, attached to the document, serves as a proof of identity and ensures the document's integrity. Verification of a digital signature involves the recipient using the sender's public key to decrypt the signature, revealing the hash value. Independently, the recipient computes the hash of the received document. If the computed hash matches the decrypted hash from the signature, it confirms that the document remains unaltered since signing and authenticates the sender.


