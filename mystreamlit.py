import streamlit as st
st.title('张恩泽')
st.header('大连理工大学')
st.subheader('帅')

st.markdowm('''
#静夜思
床前**明月**光，疑是地上霜。
举头望**明月**，低头思故乡。
''')
#markdown打印方式灵活
st.text('''
静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
''')
#text打印方式单一
 
st.markdown('**以下为打印的代码：**')
 
st.code(body:'''
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排好序，不需要再比较
        for j in range(0, n-i-1):
            # 如果元素比下一个元素大，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 示例使用
if __name__ == "__main__":
    # 测试数据
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", example_list)
    # 调用冒泡排序函数
    bubble_sort(example_list)
    print("排序后的数组:", example_list)
''', language='python')
#body要显示的代码字符串
#language代码所使用的开发语言