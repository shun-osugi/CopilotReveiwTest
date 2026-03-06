import streamlit as st


# セッションステートを初期化する処理
def init_d():
    if "t_list" not in st.session_state:
        st.session_state["t_list"] = []


# タスクを追加する関数
def add_t(name):
    # 名前が空じゃなくて、50文字以内で、タスクが100個未満なら追加
    if name != "":
        if len(name) <= 50:
            if len(st.session_state["t_list"]) < 100:
                new_id = len(st.session_state["t_list"]) + 1
                st.session_state["t_list"].append(
                    {"id": new_id, "n": name, "done": False}
                )
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# タスクを削除する処理
def del_t(id):
    new_l = []
    for i in st.session_state["t_list"]:
        if i["id"] == id:
            pass
        else:
            new_l.append(i)
    st.session_state["t_list"] = new_l


# ステータスを更新する
def update_t(id, s):
    for i in st.session_state["t_list"]:
        if i["id"] == id:
            if s == True:
                i["done"] = True
            else:
                i["done"] = False
