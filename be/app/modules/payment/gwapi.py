import pycurl
import urllib
import urllib.parse
from io import BytesIO

class gwapi():

    def __init__(self):
        self.login= dict()
        self.order = dict()
        self.billing = dict()
        self.responses = dict()

    def setLogin(self,security_key):
        self.login['security_key'] = security_key

    def setOrder(self, orderid, orderdescription, ipaddress):
        self.order['orderid'] = orderid;
        self.order['orderdescription'] = orderdescription
        self.order['ipaddress'] = ipaddress


    def setBilling(self,
            firstname,
            lastname,
            company,
            address1,
            address2,
            city,
            state,
            country,
            phone,
            email,):
        self.billing['firstname'] = firstname
        self.billing['lastname']  = lastname
        self.billing['company']   = company
        self.billing['address1']  = address1
        self.billing['address2']  = address2
        self.billing['city']      = city
        self.billing['state']     = state
        self.billing['country']   = country
        self.billing['phone']     = phone
        self.billing['email']     = email


    def doSale(self,amount, ccnumber, ccexp, cvv=''):

        query  = ""
        # Login Information

        query = query + "security_key=" + urllib.parse.quote(self.login['security_key']) + "&"
        # Sales Information
        query += "ccnumber=" + urllib.parse.quote(ccnumber) + "&"
        query += "ccexp=" + urllib.parse.quote(ccexp) + "&"
        query += "amount=" + urllib.parse.quote('{0:.2f}'.format(float(amount))) + "&"
        if (cvv!=''):
            query += "cvv=" + urllib.parse.quote(cvv) + "&"
        # Order Information
        for key,value in self.order.items():
            query += key +"=" + urllib.parse.quote(str(value)) + "&"

        # Billing Information
        for key,value in self.billing.items():
            query += key +"=" + urllib.parse.quote(str(value)) + "&"

        query += "customer_receipt=true"
        query += "type=sale"
        return self.doPost(query)



    def doPost(self,query):
        responseIO = BytesIO()
        curlObj = pycurl.Curl()
        curlObj.setopt(pycurl.POST,1)
        curlObj.setopt(pycurl.CONNECTTIMEOUT,30)
        curlObj.setopt(pycurl.TIMEOUT,30)
        curlObj.setopt(pycurl.HEADER,0)
        curlObj.setopt(pycurl.SSL_VERIFYPEER,0)
        curlObj.setopt(pycurl.WRITEFUNCTION, responseIO.write);

        curlObj.setopt(pycurl.URL,"https://secure.nmi.com/api/transact.php")

        curlObj.setopt(pycurl.POSTFIELDS,query)

        curlObj.perform()

        data = responseIO.getvalue().decode('UTF-8')
        
        temp = urllib.parse.parse_qs(data)
        for key,value in temp.items():
            self.responses[key] = value[0]
        return self.responses['response']