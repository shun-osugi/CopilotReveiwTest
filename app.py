import streamlit as st
import logic
import datetime


def main():
    st.title("高機能ToDoアプリ v2")

    logic.init_d()

    # 入力系をサイドバーに移動
    st.sidebar.header("タスクの追加")
    new_t = st.sidebar.text_input("タスク名")
    new_c = st.sidebar.selectbox("カテゴリ", st.session_state["categories"])
    new_d = st.sidebar.date_input("期限", datetime.date.today())

    if st.sidebar.button("追加"):
        res = logic.add_t(new_t, new_c, new_d)
        if res == True:
            st.sidebar.success("追加しました")
            st.rerun()
        else:
            st.sidebar.error("追加失敗")

    st.sidebar.write("---")
    if st.sidebar.button("データをJSONに保存"):
        logic.save_data()
        st.sidebar.success("data.jsonに保存しました")

    # メイン画面：絞り込みと一覧表示
    st.subheader("タスク一覧・絞り込み")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        f_s = st.selectbox("ステータス", ["すべて", "未完了", "完了"])
    with col_f2:
        f_c = st.selectbox(
            "カテゴリ絞り込み", ["すべて"] + st.session_state["categories"]
        )

    filtered_tasks = logic.filter_t(f_s, f_c)

    for t in filtered_tasks:
        col1, col2, col3, col4, col5 = st.columns([0.1, 0.4, 0.2, 0.2, 0.1])
        with col1:
            is_c = st.checkbox("", value=t["done"], key=f"chk_{t['id']}")
            if is_c != t["done"]:
                logic.update_t(t["id"], is_c)
                st.rerun()
        with col2:
            if t["done"] == True:
                st.write(f"~~{t['n']}~~")
            else:
                st.write(t["n"])
        with col3:
            st.caption(t["cat"])  # カテゴリ表示
        with col4:
            st.caption(str(t["due"]))  # 期限表示
        with col5:
            if st.button("🗑️", key=f"del_{t['id']}"):
                logic.del_t(t["id"])
                st.rerun()


if __name__ == "__main__":
    main()
