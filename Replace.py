# save the string example - The!quick!brown!fox!jumps!over!the!lazy!dog.
single_str = "The!quick!brown!fox!jumps!over!the!lazy!dog." #str sectence given
print(single_str.replace("!", " ")) #prints The quick brown fox jumps over the lazy dog
single_str =single_str.replace("!", " ") # replaces original variable with updated replaced str
print(single_str.upper()) # prints THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
print(single_str [::-1]) # prints .god yzal eht revo spmuj xof nworb kciuq ehT  this is done using slicing