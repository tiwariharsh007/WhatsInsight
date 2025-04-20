import streamlit as st
import pandas as pd
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")

st.sidebar.title("💬 WhatsApp Chat Analyzer")
st.sidebar.markdown("Upload your WhatsApp `.txt` chat file to begin!")

uploaded_file = st.sidebar.file_uploader("📎 Choose a file", type=["txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Use expander for raw chat data
    with st.expander("📄 View Raw Chat Data"):
        st.dataframe(df)

    # Unique users list
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("🔍 Analyze chat for", user_list)

    if st.sidebar.button("🧠 Show Analysis"):

        # --- Top Statistics ---
        st.markdown("## 📊 Top Statistics")
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💬 Messages", num_messages)
        col2.metric("📝 Total Words", words)
        col3.metric("📷 Media Shared", num_media_messages)
        col4.metric("🔗 Links Shared", num_links)

        # --- Most Active Users ---
        if selected_user == 'Overall':
            st.markdown("## 👥 Most Active Users")
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns([2, 1])

            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='teal')
                plt.xticks(rotation=45)
                ax.set_title("Message Count by User")
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df.style.highlight_max(axis=0))

        # --- WordCloud ---
        st.markdown("## ☁️ WordCloud of Frequent Words")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig)

        # --- Most Common Words ---
        st.markdown("## 🗣️ Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='skyblue')
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Words")
        st.pyplot(fig)

        # --- Emoji Analysis ---
        st.markdown("## 😊 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)

        # --- Monthly Timeline ---
        st.markdown("## 📆 Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green', marker='o')
        ax.set_title("Monthly Message Trend")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # --- Daily Timeline ---
        st.markdown("## 📅 Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation=45)
        ax.set_title("Daily Message Activity")
        st.pyplot(fig)

        # --- Activity Map ---
        st.markdown("## ⏰ Weekly & Monthly Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔄 Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            ax.set_ylabel("Messages")
            st.pyplot(fig)

        with col2:
            st.markdown("### 🗓️ Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            ax.set_ylabel("Messages")
            st.pyplot(fig)

        # --- Heatmap ---
        st.markdown("## 🧭 Weekly Activity Heatmap")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.heatmap(user_heatmap)
        ax.set_title("Hourly Message Heatmap")
        st.pyplot(fig)

        # --- Sentiment Analysis ---
        st.markdown("## ❤️ Sentiment Analysis")
        sentiment_df = helper.sentiment_analysis(selected_user, df)

        st.dataframe(
            sentiment_df.style.background_gradient(cmap='RdYlGn', subset=['avg_sentiment']).format({'avg_sentiment': '{:.2f}'}))
