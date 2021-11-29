import re


def email_parse(email_address):
    parsed = re.findall(r'(^[a-zA-Z0-9\.\-]+)@([a-zA-Z0-9)]+\.[a-zA-Z\.]{2,}$)', email_address)
    if not parsed:
        raise ValueError(f'wrong email: {email_address}')
    return dict(zip(["username", "domain"], parsed[0]))




print(email_parse('sdfkjh@llkdd.com'))             # OK
print(email_parse('sdfkjh@llkdd.comcom'))          # OK
print(email_parse('sdfkjh@ll555kdd.com'))          # OK
print(email_parse('sdf.kjh@llkdd.co.mm'))          # OK
print(email_parse('s-dfkjh@llkdd.co'))             # OK
print(email_parse('dflkl@kjfdg@kjkd.cmcm'))        # ValueError





