# %% [markdown]
# # Off-Platform Project: Coded Correspondence
# 
# You and your pen pal, Vishal, have been exchanging letters for some time now. Recently, he has become interested in cryptography and the two of you have started sending encoded messages within your letters.
# 
# In this project, you will use your Python skills to decipher the messages you receive and to encode your own responses! Put your programming skills to the test with these fun cryptography puzzles. Here is his most recent letter:
# 
#     Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 
# 
#     For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
#     
#         xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
#     
#     This message has an offset of 10. Can you decode it?
#     
# 
# #### Step 1: Decode Vishal's Message
# In the cell below, use your Python skills to decode Vishal's message and print the result.

# %% [markdown]
# Stuck? Open this cell to view Hints: 
# 
# <span hidden>
# You can account for shifts that go past the end of the alphabet using the modulus operator, but I'll let you figure out how!
# 
# Watch out for spaces and punctuation! Your code should only shift characters that are in the alphabet.
# 
# You'll want to find a way to represent the letters of the alphabet as numbers, where `a = 0`, `b = 1`, etc. Remember, the characters of a string can be accessed with integer indices.
# </span>

# %%
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(alphabet[0])
#print(alphabet.index('x'))
#print((alphabet.index('x') + 10)%26)
#print(alphabet[(alphabet.index('x') + 10)%26])
encoded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
#print(encoded_message[1])
decoded_message = ''
for letter in range(0, len(encoded_message)):
    if encoded_message[letter] in alphabet:
#        print(encoded_message[letter])
        decoded_message = decoded_message + alphabet[(alphabet.index(encoded_message[letter]) + 10)%26]
    else:
        decoded_message = decoded_message + encoded_message[letter]
print(decoded_message)

# %% [markdown]
# #### Step 2: Send Vishal a Coded Message
# Great job! Now send Vishal back a message using the same offset. Your message can be anything you want! Remember, encoding happens in opposite direction of decoding.

# %%
unencoded_message = 'my message back: in-a-gadda-da-vida honey, don\'tcha know that i love you? in-a-gadda-da-vida baby, don\'tcha know that i\'ll always be true?'
encoded_message = ''
for letter in range(0, len(unencoded_message)):
    if unencoded_message[letter] in alphabet:
        encoded_message = encoded_message + alphabet[(alphabet.index(unencoded_message[letter]) - 10)%26]
    else:
        encoded_message = encoded_message + unencoded_message[letter]
print(encoded_message)
# Does it work?
decoded_message = ''
for letter in range(0, len(encoded_message)):
    if encoded_message[letter] in alphabet:
#        print(encoded_message[letter])
        decoded_message = decoded_message + alphabet[(alphabet.index(encoded_message[letter]) + 10)%26]
    else:
        decoded_message = decoded_message + encoded_message[letter]
print(decoded_message)

# %% [markdown]
# #### Step 3: Make functions for decoding and coding 
# 
# Vishal sent over another reply, this time with two coded messages!
#     
#     You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with an offset of ten, and it contains a hint for decoding the second message!
# 
#     First message:
#     
#         jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
#         
#     Second message:
#     
#         bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
#     
# Decode both of these messages. 
# 
# If you haven't already, define two functions `caesar_decode(message, offset)` and `caesar_encode(message, offset)` that can be used to quickly decode and encode messages given any offset.

# %%
def caesar_decode(message, offset):
    decoded = ''
    for letter in range(0, len(message)):
        if message[letter] in alphabet:
            decoded = decoded + alphabet[(alphabet.index(message[letter]) + offset)%26]
        else:
            decoded = decoded + message[letter]
    return decoded

encoded_message = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
print(caesar_decode(encoded_message, 10))
encoded_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
print(caesar_decode(encoded_message, 14))
print()

def caesar_encode(message, offset):
    encoded = ''
    for letter in range(0, len(message)):
        if message[letter] in alphabet:
            encoded = encoded + alphabet[(alphabet.index(message[letter]) - offset)%26]
        else:
            encoded = encoded + message[letter]
    return encoded

decoded_message = 'the offset for the second message is fourteen.'
print(caesar_encode(decoded_message, 10))

# %%


# %% [markdown]
# #### Step 4: Solving a Caesar Cipher without knowing the shift value
# 
# Awesome work! While you were working to decode his last two messages, Vishal sent over another letter! He's really been bitten by the crypto-bug. Read it and see what interesting task he has lined up for you this time.
# 
#     Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
#             
#     To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. You'll have to brute force it yourself.
#             
#     Here's the coded message:
#             
#         vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
#             
#     Good luck!
#             
# Decode Vishal's most recent message and see what it says!

# %% [markdown]
# Stuck? Open this cell to view Hints: 
# 
# <span hidden>
# Since you don't know the cipher's offset, you'll need to try every possible option until you find the right one. Use a Python statement that will allow you to execute `caesar_decode()` multiple times with different `offset` arguments.
# </span>

# %%
encoded_message = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
for shift in range(1, len(alphabet) + 1):
    print(caesar_decode(encoded_message, shift))
print()
print(caesar_decode(encoded_message, 7))

# %% [markdown]
# #### Step 5: The Vigenère Cipher
# 
# Great work! While you were working on the brute force cracking of the cipher, Vishal sent over another letter. That guy is a letter machine!
# 
#     Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#             
#     The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
#            
#     Consider the message:
#            
#         barry is the spy
# 
#     If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
#            
#         dog
#                
#     Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.
# 
#                   message:    b  a  r  r  y    i  s    t  h  e    s  p  y
#                 
#            keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
#                  
#     resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
#       
#     So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 24, which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 15, and get "l", shift the next "r" by 4 places and get "o", and so forth. Once we complete all the shifts we end up with our coded message:
#             
#         ymlok cp fbb ejv
#                 
#     As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
#             
#         txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!
#                 
#     and the keyword to decode my message is 
#             
#         friends
#                 
#     Because that's what we are! Good luck friend!
#            
# And there it is. Vishal has given you quite the assignment this time! Try to decode his message. It may be helpful to create a function that takes two parameters &mdash; the coded message and the keyword &mdash; then work towards a solution from there.

# %% [markdown]
# Stuck? Open this cell to view Hints: 
# 
# <span hidden>
# Like before, you'll only want to shift characters that are in the alphabet. Your keyword phrase should ignore any spaces and punctuation in the original message.
# 
# For example, given the message
# 
#   ciphers are awesome!
# 
# and the keyword
# 
#   cat
# 
# the keyword phrase would be:
# 
#   catcatc atc atcatca
# 
# and the encoded string would be:
# 
#   aiwfeyq ayc adcsvke!
# </span>

# %%
def vigenere(msg, kyd):
    keyword_extended = ''
    kw_letter = 0
    for letter in range(0, len(msg)):
        if msg[letter] in alphabet:
            keyword_extended = keyword_extended + kyd[kw_letter % len(kyd)]
            kw_letter += 1
        else:
            keyword_extended = keyword_extended + msg[letter]
    clear_message = ''
    for letter in range(0, len(msg)):
        if msg[letter] in alphabet:
            clear_message = clear_message + alphabet[(alphabet.index(msg[letter]) + alphabet.index(keyword_extended[letter]))%26]
        else:
            clear_message = clear_message + msg[letter]
    return clear_message

encoded_message = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!'
keyword = 'friends'
print(vigenere(encoded_message, keyword))

# %% [markdown]
# #### Step 6: Send a message with the  Vigenère Cipher
# Great work decoding the message. For your final task, write a function that can encode a message using a given keyword and write out a message to send to Vishal!
# 
# *As a bonus, try calling your decoder function on the result of your encryption function. You should get the original message back!*

# %%
lyric = 'Oh cryin\' won\'t help you, prayin\' won\'t do no good\nOh cryin\' won\'t help you, prayin\' won\'t do no good\nWhen the levee breaks, mama, you got to lose'
keyword = 'minnie'

extended_kyd = ''
kyd_letter_ctr = 0
for letter in range(0, len(lyric)):
    if lyric[letter] in alphabet:
        extended_kyd = extended_kyd + keyword[kyd_letter_ctr % len(keyword)]
        kyd_letter_ctr += 1
    else:
        extended_kyd = extended_kyd + lyric[letter]
encoded_message = ''
for letter in range(0, len(lyric)):
    if lyric[letter] in alphabet:
        encoded_message = encoded_message + alphabet[(alphabet.index(lyric[letter]) - alphabet.index(extended_kyd[letter]))%26]
    else:
        encoded_message = encoded_message + lyric[letter]
print(encoded_message)
print()

print(vigenere(encoded_message, keyword))

# %% [markdown]
# #### Conclusion
# Over the course of this project you've learned about two different cipher methods and have used your Python skills to code and decode messages. There are all types of other facinating ciphers out there to explore, and Python is the perfect language to implement them with, so go exploring! 


