import sqlalchemy as db
import requests
from sqlalchemy import update
import logging, time, os

class Connection:
    def get_connection(self, user, password, host, port, database):
        return db.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))

    def get_dissconnected(self):
        return engine.dispose()

class logFile():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    dirName = "logs"
    fileName = "mycode"
    timeStamp = time.strftime("%Y-%m-%d %H:%M:%S")
    logFQ = dirName + "/" + fileName + "_" + timeStamp + ".log"
    logging.basicConfig(datefmt='%m-%d %H:%M:%S', filename=logFQ, format='%(asctime)s %(message)s', filemode='w', level=logging.INFO)

    def loggingLogs(self):
        return logging.getLogger()

class handlingData:
    def metadata(self):
        meta_data = db.MetaData(bind=c)
        db.MetaData.reflect(meta_data)
        urlList = meta_data.tables['urlValidation']
        return urlList

    def updateStatus(self, ch, id):
        urlList = self.metadata()
        upd = update(urlList)

        if ch == 1:
            val = upd.values({"status":"valid"})
            cod = val.where(urlList.c.id == id)
            c.execute(cod)
        
        elif ch == 2:
            val = upd.values({"status":"invalid"})
            cod = val.where(urlList.c.id == id)
            c.execute(cod)

    def url_checker(self, url, id):
        try:
            #Get Url
            get = requests.get(url)
            # if the request succeeds 
            if get.status_code == 200:
                lg.info("Valid")
                # print("Valid")
                # return(print(f"{url}: is reachable"))
                self.updateStatus(1, id)

            else:
                lg.info("InValid")
                # print("InValid")
                lg.info(f"{url}: is Not reachable, status_code: {get.status_code}")
                # print(f"{url}: is Not reachable, status_code: {get.status_code}")
                self.updateStatus(1, id)
                # return(print(f"{url}: is Not reachable, status_code: {get.status_code}"))

        except requests.exceptions.RequestException as e:
            # print URL with Errs
            lg.warning(f"NotReachable {e}")
            # print("NotReachable", e)
            self.updateStatus(2, id)
            # raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

    def getUrlList(self):
        urlList = self.metadata()
        query = db.select([urlList.c.id, urlList.c.url])
        result = c.execute(query).fetchall()
        
        for record in result:
            lg.info(record[1])
            # print(record[1])
            self.url_checker(record[1], record[0])



if __name__ == '__main__':
    
    user = 'root'
    password = 'flame'
    host = '127.0.0.1'
    port = 3306
    database = 'jio_demo'

    try:
        connect = Connection()
        engine = connect.get_connection(user, password, host, port, database)
        c = engine.connect()
        log = logFile()
        lg = log.loggingLogs()
        
        lg.info(f"Connection to the {host} for user {user} created successfully.")
        # print(f"Connection to the {host} for user {user} created successfully.")

        getList = handlingData()
        getList.getUrlList()
        c.close()
        connect.get_dissconnected()
        lg.info("Connection disabled")
        # print("Connection disabled")
        # getList.getUrlList()

    except Exception as ex:
        lg.error("Connection could not be made due to the following error: \n", ex)
        # print("Connection could not be made due to the following error: \n", ex)
