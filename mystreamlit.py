import streamlit as st
st.title('�Ŷ���')
st.header('��������ѧ')
st.subheader('˧')

st.markdowm('''
#��ҹ˼
��ǰ**����**�⣬���ǵ���˪��
��ͷ��**����**����ͷ˼���硣
''')
#markdown��ӡ��ʽ���
st.text('''
��ҹ˼
��ǰ���¹⣬���ǵ���˪��
��ͷ�����£���ͷ˼���硣
''')
#text��ӡ��ʽ��һ
 
st.markdown('**����Ϊ��ӡ�Ĵ��룺**')
 
st.code(body:'''
def bubble_sort(arr):
    n = len(arr)
    # ������������Ԫ��
    for i in range(n):
        # ��� i ��Ԫ���Ѿ��ź��򣬲���Ҫ�ٱȽ�
        for j in range(0, n-i-1):
            # ���Ԫ�ر���һ��Ԫ�ش��򽻻�����
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# ʾ��ʹ��
if __name__ == "__main__":
    # ��������
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("ԭʼ����:", example_list)
    # ����ð��������
    bubble_sort(example_list)
    print("����������:", example_list)
''', language='python')
#bodyҪ��ʾ�Ĵ����ַ���
#language������ʹ�õĿ�������