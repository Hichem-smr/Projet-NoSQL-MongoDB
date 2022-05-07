import sys
from PyQt5 import QtWidgets
from interface import Ui_MainWindow
import pymongo
from pymongo import MongoClient
import world
import qdarktheme
from manual import Ui_Dialog


class Window2(QtWidgets.QDialog):                           # <===
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



class myApp(QtWidgets.QMainWindow):
        ww = None

        def __init__(self):
            super(myApp, self).__init__()
            
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self)
            
            row = 1
            for x in MongoClient().list_database_names():
                pays = QtWidgets.QTreeWidgetItem(self.ui.DB_tree)
                pays.setText(0, str(x))
                row += 1


            self.ui.QueryExecute.clicked.connect(self.execute)
            self.ui.Connect_db.clicked.connect(self.connect)
            self.ui.Disconnect_db.clicked.connect(self.Disconnect)
            self.ui.Manual.clicked.connect(self.man)
            self.ui.req_1.toggled.connect(self.activation)
            self.ui.req_2.toggled.connect(self.activation)
            self.ui.req_3.toggled.connect(self.activation)
            self.ui.req_4.toggled.connect(self.activation)
            self.ui.req_5.toggled.connect(self.activation)
            self.ui.req_6.toggled.connect(self.activation)
            self.ui.req_7.toggled.connect(self.activation)
            self.ui.req_8.toggled.connect(self.activation)
            self.ui.req_9.toggled.connect(self.activation)
            self.ui.req_10.toggled.connect(self.activation)
            self.ui.req_11.toggled.connect(self.activation)
            self.ui.req_12.toggled.connect(self.activation)
            self.ui.req_13.toggled.connect(self.activation)
            self.ui.req_14.toggled.connect(self.activation)
            self.ui.req_15.toggled.connect(self.activation)

        def man(self):                                            
            self.w = Window2()
            self.w.show()
        
        def connect(self):
            global ww
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            item = self.ui.DB_tree.currentItem()
            selected = item.text(0)
            BDD = myclient[selected]
            ww = BDD["world"]
            self.ui.req_1.setEnabled(True)
            self.ui.req_2.setEnabled(True)
            self.ui.req_3.setEnabled(True)
            self.ui.req_4.setEnabled(True)
            self.ui.req_5.setEnabled(True)
            self.ui.req_6.setEnabled(True)
            self.ui.req_7.setEnabled(True)
            self.ui.req_8.setEnabled(True)
            self.ui.req_9.setEnabled(True)
            self.ui.req_10.setEnabled(True)
            self.ui.req_11.setEnabled(True)
            self.ui.req_12.setEnabled(True)
            self.ui.req_13.setEnabled(True)
            self.ui.req_14.setEnabled(True)
            self.ui.req_15.setEnabled(True)
            self.ui.Disconnect_db.setEnabled(True)


        def activation(self):
            self.ui.QueryExecute.setEnabled(True)
            

        def Disconnect(self):
            global ww
            self.ui.Disconnect_db.setEnabled(False)
            ww = None
            self.ui.TableQuery.clearContents()
            self.ui.req_1.setEnabled(False)
            self.ui.req_2.setEnabled(False)
            self.ui.req_3.setEnabled(False)
            self.ui.req_4.setEnabled(False)
            self.ui.req_5.setEnabled(False)
            self.ui.req_6.setEnabled(False)
            self.ui.req_7.setEnabled(False)
            self.ui.req_8.setEnabled(False)
            self.ui.req_9.setEnabled(False)
            self.ui.req_10.setEnabled(False)
            self.ui.req_11.setEnabled(False)
            self.ui.req_12.setEnabled(False)
            self.ui.req_13.setEnabled(False)
            self.ui.req_14.setEnabled(False)
            self.ui.req_15.setEnabled(False)

            self.ui.req_1.setAutoExclusive(False)
            self.ui.req_1.setChecked(False)
            self.ui.req_1.setAutoExclusive(True)
            self.ui.req_2.setAutoExclusive(False)
            self.ui.req_2.setChecked(False)
            self.ui.req_2.setAutoExclusive(True)
            self.ui.req_3.setAutoExclusive(False)
            self.ui.req_3.setChecked(False)
            self.ui.req_3.setAutoExclusive(True)
            self.ui.req_4.setAutoExclusive(False)
            self.ui.req_4.setChecked(False)
            self.ui.req_4.setAutoExclusive(True)
            self.ui.req_5.setAutoExclusive(False)
            self.ui.req_5.setChecked(False)
            self.ui.req_5.setAutoExclusive(True)
            self.ui.req_6.setAutoExclusive(False)
            self.ui.req_6.setChecked(False)
            self.ui.req_6.setAutoExclusive(True)
            self.ui.req_7.setAutoExclusive(False)
            self.ui.req_7.setChecked(False)
            self.ui.req_7.setAutoExclusive(True)
            self.ui.req_8.setAutoExclusive(False)
            self.ui.req_8.setChecked(False)
            self.ui.req_8.setAutoExclusive(True)
            self.ui.req_9.setAutoExclusive(False)
            self.ui.req_9.setChecked(False)
            self.ui.req_9.setAutoExclusive(True)
            self.ui.req_10.setAutoExclusive(False)
            self.ui.req_10.setChecked(False)
            self.ui.req_10.setAutoExclusive(True)
            self.ui.req_11.setAutoExclusive(False)
            self.ui.req_11.setChecked(False)
            self.ui.req_11.setAutoExclusive(True)
            self.ui.req_12.setAutoExclusive(False)
            self.ui.req_12.setChecked(False)
            self.ui.req_12.setAutoExclusive(True)
            self.ui.req_13.setAutoExclusive(False)
            self.ui.req_13.setChecked(False)
            self.ui.req_13.setAutoExclusive(True)
            self.ui.req_14.setAutoExclusive(False)
            self.ui.req_14.setChecked(False)
            self.ui.req_14.setAutoExclusive(True)
            self.ui.req_15.setAutoExclusive(False)
            self.ui.req_15.setChecked(False)
            self.ui.req_15.setAutoExclusive(True)

            self.ui.QueryExecute.setEnabled(False)


        def execute(self):
            if self.ui.req_1.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Nombre_Pays'])
                self.ui.TableQuery.setRowCount(1)

                result = world.Question1(ww)
                it = QtWidgets.QTableWidgetItem(result)
                self.ui.TableQuery.setItem(0, 0, it)
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_2.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Continents'])
                
                results = world.Question2(ww)
                self.ui.TableQuery.setRowCount(len(results))
                row = 0
                for result in results:
                    it = QtWidgets.QTableWidgetItem(result)
                    self.ui.TableQuery.setItem(row, 0, it)
                    row +=1
                self.ui.TableQuery.resizeColumnsToContents()
            
            elif self.ui.req_3.isChecked():    
                labels = ["Name", "Code", "Continent", "Region", "Surface", "IndepYear", "Population", "LifeExpectancy", "GNP", "LocalName", "Code2", "Capital", "GovernmentForm"   ]
                result = world.Question3(ww)
                self.ui.TableQuery.setColumnCount(13)
                self.ui.TableQuery.setRowCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                self.ui.TableQuery.setItem(0, 0, QtWidgets.QTableWidgetItem(result["Name"]))
                self.ui.TableQuery.setItem(0, 1, QtWidgets.QTableWidgetItem(result["Code"]))
                self.ui.TableQuery.setItem(0, 2, QtWidgets.QTableWidgetItem(result["Continent"]))
                self.ui.TableQuery.setItem(0, 3, QtWidgets.QTableWidgetItem(result["Region"]))
                self.ui.TableQuery.setItem(0, 4, QtWidgets.QTableWidgetItem(str(result["SurfaceArea"])))
                self.ui.TableQuery.setItem(0, 5, QtWidgets.QTableWidgetItem(str(result["IndepYear"])))
                self.ui.TableQuery.setItem(0, 6, QtWidgets.QTableWidgetItem(str(result["Population"])))
                self.ui.TableQuery.setItem(0, 7, QtWidgets.QTableWidgetItem(str(result["LifeExpectancy"])))
                self.ui.TableQuery.setItem(0, 8, QtWidgets.QTableWidgetItem(str(result["GNP"])))
                self.ui.TableQuery.setItem(0, 9, QtWidgets.QTableWidgetItem(result["LocalName"]))
                self.ui.TableQuery.setItem(0, 10, QtWidgets.QTableWidgetItem(result["Code2"]))
                self.ui.TableQuery.setItem(0, 11, QtWidgets.QTableWidgetItem(result["Capital"]["Name"]))
                self.ui.TableQuery.setItem(0, 12, QtWidgets.QTableWidgetItem(result["GovernmentForm"]))
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_4.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Pays'])
                
                results = world.Question4(ww)
                self.ui.TableQuery.setRowCount(3)
                row = 0
                for result in list(results):
                    it = QtWidgets.QTableWidgetItem(result['Name'])
                    self.ui.TableQuery.setItem(row, 0, it)
                    row +=1
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_5.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Pays Independants'])
                
                results = world.Question5(ww)
                self.ui.TableQuery.setRowCount(len(results))
                row = 0
                for result in results:
                    it = QtWidgets.QTableWidgetItem(result)
                    self.ui.TableQuery.setItem(row, 0, it)
                    row +=1
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_6.isChecked():
                labels = ["Continent", "Surface"]
                self.ui.TableQuery.setColumnCount(2)
                result = list(world.question6(ww))[0]
                self.ui.TableQuery.setRowCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                self.ui.TableQuery.setItem(0, 0, QtWidgets.QTableWidgetItem(result["_id"]))
                self.ui.TableQuery.setItem(0, 1, QtWidgets.QTableWidgetItem(str(result['SurfaceArea'])))
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_7.isChecked():
                labels = ["Continent", "Population", "Pays", "IndepPays"]
                self.ui.TableQuery.setColumnCount(4)
                results = list(world.question7(ww))
                self.ui.TableQuery.setRowCount(len(results))
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                row = 0
                for result in results:
                    self.ui.TableQuery.setItem(row, 0, QtWidgets.QTableWidgetItem(result["_id"]))
                    self.ui.TableQuery.setItem(row, 1, QtWidgets.QTableWidgetItem(str(result['Population_Total'])))
                    self.ui.TableQuery.setItem(row, 2, QtWidgets.QTableWidgetItem(str(result['Pays'])))
                    self.ui.TableQuery.setItem(row, 3, QtWidgets.QTableWidgetItem(str(result['Pays_indep'])))
                    row += 1
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_8.isChecked():
                results = list(world.question8(ww))
                self.ui.TableQuery.setColumnCount(2)
                self.ui.TableQuery.setRowCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(["Sans capital", "Avec capital"])
                self.ui.TableQuery.setItem(0, 0, QtWidgets.QTableWidgetItem(str(results[0])))
                self.ui.TableQuery.setItem(0, 1, QtWidgets.QTableWidgetItem(str(results[1])))
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_9.isChecked():
                results = list(world.question9(ww))
                self.ui.TableQuery.setColumnCount(2)
                self.ui.TableQuery.setRowCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(["Capital", "Population"])
                self.ui.TableQuery.setItem(0, 0, QtWidgets.QTableWidgetItem(str(results[0])))
                self.ui.TableQuery.setItem(0, 1, QtWidgets.QTableWidgetItem(str(results[1])))
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_10.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Langues'])
                results = world.question10(ww)
                self.ui.TableQuery.setRowCount(len(results))
                row = 0
                for result in list(results):
                    it = QtWidgets.QTableWidgetItem(result)
                    self.ui.TableQuery.setItem(row, 0, it)
                    row +=1
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_11.isChecked():
                self.ui.TableQuery.setColumnCount(1)
                self.ui.TableQuery.setHorizontalHeaderLabels(['Pays'])
                results = world.question11(ww)
                self.ui.TableQuery.setRowCount(len(results))
                row = 0
                for result in list(results):
                    it = QtWidgets.QTableWidgetItem(result)
                    self.ui.TableQuery.setItem(row, 0, it)
                    row +=1
                self.ui.TableQuery.resizeColumnsToContents()

            elif self.ui.req_12.isChecked():
                labels = ["City", "Population", "Pays"]
                self.ui.TableQuery.setColumnCount(3)
                results = list(world.question12(ww))
                self.ui.TableQuery.setRowCount(len(results))
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                row = 0
                for result in results:
                    self.ui.TableQuery.setItem(row, 0, QtWidgets.QTableWidgetItem(result["Cities"]["Name"]))
                    self.ui.TableQuery.setItem(row, 1, QtWidgets.QTableWidgetItem(str(result['Cities']["Population"])))
                    self.ui.TableQuery.setItem(row, 2, QtWidgets.QTableWidgetItem(str(result['Name'])))
                    row += 1
                self.ui.TableQuery.resizeColumnsToContents()
            elif self.ui.req_13.isChecked():
                labels = ["Pays"]
                self.ui.TableQuery.setColumnCount(1)
                results = list(world.question13(ww))
                self.ui.TableQuery.setRowCount(len(results))
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                row = 0
                for result in results:
                    self.ui.TableQuery.setItem(row, 0, QtWidgets.QTableWidgetItem(result))
                    row += 1
                self.ui.TableQuery.resizeColumnsToContents()
            elif self.ui.req_14.isChecked():
                labels = ["Pays", "Nombre de langues"]
                self.ui.TableQuery.setColumnCount(2)
                results = list(world.question14(ww))
                self.ui.TableQuery.setRowCount(len(results))
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                row = 0
                for result in results:
                    self.ui.TableQuery.setItem(row, 0, QtWidgets.QTableWidgetItem(result))
                    self.ui.TableQuery.setItem(row, 1, QtWidgets.QTableWidgetItem("12"))
                    row += 1
                self.ui.TableQuery.resizeColumnsToContents()
            elif self.ui.req_15.isChecked():
                labels = ["Pays", "Population_total", "Population des villes"]
                self.ui.TableQuery.setColumnCount(3)
                results = list(world.question15(ww))
                self.ui.TableQuery.setRowCount(len(results))
                self.ui.TableQuery.setHorizontalHeaderLabels(labels)
                row = 0
                for result in results:
                    self.ui.TableQuery.setItem(row, 0, QtWidgets.QTableWidgetItem(result["name"]))
                    self.ui.TableQuery.setItem(row, 1, QtWidgets.QTableWidgetItem(str(result["population"])))
                    self.ui.TableQuery.setItem(row, 2, QtWidgets.QTableWidgetItem(str(result["villes"])))
                    row += 1
                self.ui.TableQuery.resizeColumnsToContents()

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    win.show()
    sys.exit(app.exec_())

app()