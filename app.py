from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'hello world'

@FAI.route('/wishing')
def wishing():
    return 'welcome to flask project'

if __name__=='__main__':
    FAI.run(debug=True)