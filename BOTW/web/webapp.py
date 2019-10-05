from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import unicodedata
import base64
import os
#from merkle import merkleTree
#from alicia import alicia_encrypt
app = Flask(__name__)

@app.route('/home')
def student():
  return render_template('index.html')

@app.route('/getcustomerdata', methods=['POST'])
def getcdata():
    if request.method=='POST':
        result=request.form
        cname=result['cid']
        print cname
        r=requests.get(url = 'http://52.168.129.85:3000/api/org.acme.tracker.Customer/'+str(cname))
        res=r.json()
        print res
        return render_template('showCustomer.html', info=res)
@app.route('/getloandata', methods=['POST'])
def getcdata():
    if request.method=='POST':
        result=request.form
        cname=result['cid']
        print cname
        r=requests.get(url = 'http://52.168.129.85:3000/api/queries/selectLoanByCustomer?customerId='+str(cname))
        res=r.json()
        print res
        return render_template('showcLoan.html', info=res)
@app.route('/getpaymentdata', methods=['POST'])
def getcdata():
    if request.method=='POST':
        result=request.form
        cname=result['cid']
        print cname
        r=requests.get(url = 'http://52.168.129.85:3000/api/queries/selectPaymentRecordByCustomer?customerId='+str(cname))
        res=r.json()
        print res
        return render_template('showPayment.html', info=res)
app.route('/gettitledata', methods=['POST'])
def getcdata():
    if request.method=='POST':
        result=request.form
        cname=result['cid']
        print cname
        r=requests.get(url = 'http://52.168.129.85:3000/api/queries/selectTitleByCustomer?customerId='+str(cname))
        res=r.json()
        print res
        return render_template('showTitle.html', info=res)
app.route('/transfertitle', methods=['POST'])
def getcdata():
    if request.method=='POST':
        result=request.form
        cname=result['cid']
        print cname
        r=requests.get(url = 'http://52.168.129.85:3000/api/org.acme.tracker.titletransfer/'+str(cname))
        res=r.json()
        print res
        return render_template('showTitleStatus.html', info=res)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5600)
