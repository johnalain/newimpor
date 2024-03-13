n: int = 1000000000
print(f'{n:_}')
# add seperator output:1_000_000_000
print(f'{n:,}')
#output seperator:1,000,000,000
# above are two seperators can be used with python 
var: str = 'var'
print(f'{var:>20}:')
# output:with 20 space var:
print(f'{var:<20}:')#output:
                #  var:
# var                 :
print(f'{var:20}:')
# var                : 
print(f'{var:^20}:')
        # var         :
print(f'{var:_<20}:')
print(f'{var:#>20}:')
print(f'{var:|^20}:')
#output
# var_________________:
# #################var:
# ||||||||var|||||||||: