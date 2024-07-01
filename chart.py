import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout
from PyQt5.QtChart import QChartView, QChart, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class Ui_Dialog(object):
    def setupUi(self, Dialog, data_dict):
        Dialog.setWindowTitle("CHART VIEW")
        Dialog.resize(580, 420)

        layout = QVBoxLayout(Dialog)
        chart = QChart()
        chart.setTitle("CHART VIEW")
        self.chartView = QChartView(Dialog)
        self.chartView.setChart(chart)
        layout.addWidget(self.chartView)

        bar_set = QBarSet("Occurrences")
        for key in range(1, 11):
            bar_set.append(data_dict.get(key, 0))

        series = QBarSeries()
        series.append(bar_set)
        chart.addSeries(series)

        #
        axisX = QBarCategoryAxis()
        axisX.append([str(i) for i in range(1, 11)])
        axisX.setTitleText("Category ID")

        axisY = QValueAxis()
        axisY.setTitleText("Occurrences")
        axisY.setRange(0, max(data_dict.values()) + 1)  # 动态设置Y轴范围

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)

        self.save_chart_as_image()

    def save_chart_as_image(self):    #source : https://blog.csdn.net/guo763199198/article/details/114011995
        pixmap = self.chartView.grab()

        image = pixmap.toImage()

        image.save("chart.png")

def create_and_save_chart(data_dict):
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, data_dict)

    # 显示窗口并保持可见
    Dialog.show()
    sys.exit(app.exec_())
