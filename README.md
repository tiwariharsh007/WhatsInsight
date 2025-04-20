# WhatsInsight 📊

WhatsInsight is an interactive web application built using **Streamlit** that allows users to analyze **WhatsApp chat data** at both **individual** and **group** levels. Just upload your exported `.txt` chat file and get detailed visual insights into your conversations.

---

## 🔍 Key Features

- **👤 Group & Individual Chat Analysis**  
  Analyze data for specific individuals or the entire group using a user dropdown.

- **📄 Raw Chat Viewer**  
  Raw data is neatly displayed inside an expandable section, keeping the UI clean.

- **📊 Top Statistics**  
  Quickly view:

  - Total messages sent
  - Total words used
  - Media shared (images, videos)
  - Links shared

- **👥 Most Active Users** _(For Group Chats)_  
  Visual and tabular representation of the most active participants.

- **☁️ WordCloud of Frequent Words**  
  Generates a word cloud to visualize the most used words in the chat.

- **🗣️ Most Common Words**  
  Bar chart showing the most frequently used words and their counts.

- **😊 Emoji Analysis**  
  Breakdown of emojis used in the chat along with a pie chart visualization.

- **📆 Monthly Timeline**  
  Trend analysis of the number of messages sent each month.

- **📅 Daily Timeline**  
  Message activity visualized day-by-day for granular analysis.

- **⏰ Weekly & Monthly Activity Maps**  
  Identify the most active:

  - Days of the week
  - Months of the year

- **🧭 Weekly Activity Heatmap**  
  Heatmap of messages sent at different times of day throughout the week.

- **❤️ Sentiment Analysis**  
  Uses NLP to evaluate the sentiment (positive, neutral, or negative) of chat messages.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**
- **TextBlob**
- **Regex**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/WhatsInsight.git
cd WhatsInsight
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 🗂️ File Format

Make sure your WhatsApp chat is exported as a `.txt` file (without media).

---
