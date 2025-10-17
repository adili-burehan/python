import flet as ft


def main(page):
    page.title = "测试应用"

    # 最简单的应用，避免所有可能的属性错误
    page.add(
        ft.Column([
            ft.Text("应用运行成功!", size=24),
            ft.TextField(label="输入框"),
            ft.ElevatedButton("点击我"),
            ft.Checkbox(label="选项", value=True),
        ])
    )


ft.app(main)
