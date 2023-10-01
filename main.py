from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

"""
创建应用步骤：
    1. 基于 App 类创建一个子类 MainApp。
    2. build() 方法返回一个控件实例，即整个应用的根控件。
    3. 创建 MainApp 实例，调用 run() 方法。
"""


class MainApp(App):
    def build(self):
        # icon
        # self.icon = 'xx.png'
        # 运算符
        self.operators = ["/", "*", "+", "-"]
        # 记录最后点击的按钮
        self.last_button = None
        # 最后点击是否为运算符
        self.last_was_operator = None
        # 根控件，其子元素垂直排列在框中
        main_layout = BoxLayout(orientation="vertical")
        # 添加输入显示框到根控件
        self.solution = TextInput(
            background_color="black",
            foreground_color="white",
            multiline=False,
            halign="right",
            font_size=55,
            readonly=True,
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "5", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]
        # 添加按钮
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    background_color="grey",
                    # pos_hint 设置控件在其父布局中的位置
                    pos_hint={
                        "center_x": 0.5,
                        "center_y": 0.5,
                    },
                )
                # 绑定点击事件
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # 添加"="按钮
        equal_button = Button(
            text="=",
            font_size=30,
            background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        """
        按钮点击事件
        """
        current = self.solution.text
        button_text = instance.text

        # 清除
        if button_text == "C":
            self.solution.text = ""
        # 重复点击运算符
        elif current and (self.last_was_operator and button_text in self.operators):
            return
        # 点击运算符
        elif current == "" and button_text in self.operators:
            return
        # 拼接输入
        else:
            new_text = current + button_text
            self.solution.text = new_text

        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

    def on_solution(self, instance):
        """
        “=”按钮点击事件
        """
        text = self.solution.text
        if text:
            solution = str(eval(text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
