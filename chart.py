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

        # 创建一个QBarSet并添加数据
        bar_set = QBarSet("Occurrences")
        for key in range(1, 11):
            bar_set.append(data_dict.get(key, 0))

        # 创建一个QBarSeries并添加QBarSet
        series = QBarSeries()
        series.append(bar_set)
        chart.addSeries(series)

        # 设置X轴
        axisX = QBarCategoryAxis()
        axisX.append([str(i) for i in range(1, 11)])
        axisX.setTitleText("Category ID")

        # 设置Y轴
        axisY = QValueAxis()
        axisY.setTitleText("Occurrences")
        axisY.setRange(0, max(data_dict.values()) + 1)  # 动态设置Y轴范围

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)

        # 保存图像并显示对话框
        self.save_chart_as_image()

    def save_chart_as_image(self):
        # Capture the chart view as a QPixmap
        pixmap = self.chartView.grab()

        # Convert QPixmap to QImage
        image = pixmap.toImage()

        # Save the QImage to a file
        image.save("chart.png")

def create_and_save_chart(data_dict):
    app = QApplication.instance()  # Use existing QApplication instance if available
    if app is None:
        app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, data_dict)

    # 显示窗口并保持可见
    Dialog.show()
    app.exec_()

if __name__ == "__main__":
    # 示例数据字典
    data_dict = {
        1: 4,
        2: 7,
        3: 5,
        4: 3,
        5: 6,
        6: 2,
        7: 1,
        8: 9,
        9: 8,
        10: 4
    }

    create_and_save_chart(data_dict)
