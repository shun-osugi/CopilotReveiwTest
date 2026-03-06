import streamlit as st
import logic


def main():
    st.title("シンプルToDoアプリ")

    # データの初期化
    logic.init_d()

    # Create (作成)
    new_t = st.text_input("新しいタスクを入力してください")
    if st.button("追加"):
        res = logic.add_t(new_t)
        if res == True:
            st.success("タスクを追加しました！")
            st.rerun()
        else:
            st.error("エラー：追加できませんでした。")

    st.write("---")
    st.subheader("タスク一覧")

    # Read (読み取り) と Update/Delete
    for t in st.session_state["t_list"]:
        # Streamlitのカラム機能でUIを整える
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        with col1:
            # Update (更新)
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
            # Delete (削除)
            if st.button("削除", key=f"del_{t['id']}"):
                logic.del_t(t["id"])
                st.rerun()


if __name__ == "__main__":
    main()
