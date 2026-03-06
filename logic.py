import streamlit as st
import datetime
import json


def init_d():
    if "t_list" not in st.session_state:
        st.session_state["t_list"] = []
    # 新機能: カテゴリの初期化
    if "categories" not in st.session_state:
        st.session_state["categories"] = ["仕事", "プライベート", "その他"]


# 新機能: カテゴリ(cat)と期限(due_date)を追加
def add_t(name, cat, due_date):
    # 意図的な深いネスト（早期リターン違反）
    if name != "":
        if len(name) <= 50:
            if len(st.session_state["t_list"]) < 100:
                if cat in st.session_state["categories"]:
                    new_id = len(st.session_state["t_list"]) + 1  # 意図的なID採番バグ
                    st.session_state["t_list"].append(
                        {
                            "id": new_id,
                            "n": name,
                            "cat": cat,
                            "due": str(due_date),
                            "done": False,
                        }
                    )
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def del_t(id):
    new_l = []
    for i in st.session_state["t_list"]:
        if i["id"] == id:
            pass
        else:
            new_l.append(i)
    st.session_state["t_list"] = new_l


def update_t(id, s):
    for i in st.session_state["t_list"]:
        if i["id"] == id:
            if s == True:
                i["done"] = True
            else:
                i["done"] = False


# 新機能: タスクの絞り込み（冗長な真偽値判定のオンパレード）
def filter_t(status_filter, cat_filter):
    res = []
    for t in st.session_state["t_list"]:
        match_status = False
        if status_filter == "すべて":
            match_status = True
        elif status_filter == "完了":
            if t["done"] == True:
                match_status = True
        elif status_filter == "未完了":
            if t["done"] == False:
                match_status = True

        match_cat = False
        if cat_filter == "すべて":
            match_cat = True
        elif t["cat"] == cat_filter:
            match_cat = True

        if match_status == True:
            if match_cat == True:
                res.append(t)
    return res


# 新機能: データ保存モック
def save_data():
    d = st.session_state["t_list"]
    with open("data.json", "w") as f:
        f.write(json.dumps(d))
    return True
