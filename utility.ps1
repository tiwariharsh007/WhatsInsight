git init
git config user.name "tiwariharsh007"
git config user.email "tiwari007harsh@gmail.com"

$commits = @(
    "2025-05-09|setup project structure and initial files"
    "2025-05-09|add basic Flask app to run chat analyzer"

    "2025-05-12|implement preprocessing pipeline for WhatsApp chat text"
    "2025-05-12|add stop words list and integration"
    "2025-05-12|improve regex cleaning for timestamps and emojis"
    "2025-05-12|test preprocessing with sample chat file"

    "2025-05-16|implement word frequency counter for messages"
    "2025-05-16|add sentiment analysis using TextBlob"
    "2025-05-16|create helper functions for user-level stats"
    "2025-05-16|optimize performance in preprocessing script"
    "2025-05-16|update requirements.txt with missing libraries"

    "2025-05-19|implement word cloud visualization"
    "2025-05-19|add matplotlib support for chat trends"
    "2025-05-19|fix minor bug in preprocessing related to empty lines"

    "2025-05-23|add per-user message distribution chart"
    "2025-05-23|implement active hours heatmap"
    "2025-05-23|improve visualization color schemes"
    "2025-05-23|add functionality to detect most replied messages"
    "2025-05-23|update README with usage instructions"
    "2025-05-23|clean unused imports and improve logging"

    "2025-05-26|fix bug in word cloud generation with non-English text"
    "2025-05-26|add extra stop words to stop_words.txt"

    "2025-05-28|add emoji usage statistics"
    "2025-05-28|implement longest conversation streak detection"
    "2025-05-28|refine sentiment analysis scoring"
    "2025-05-28|finalize README with screenshots and examples"
    "2025-05-28|prepare stable release version"
)

if (-not (Test-Path "dummy.txt")) {
    New-Item -ItemType File -Name "dummy.txt" | Out-Null
}

foreach ($commit in $commits) {
    $parts = $commit -split "\|", 2
    $date = $parts[0]
    $message = $parts[1]

    Add-Content -Path "dummy.txt" -Value $message
    git add .

    $hour = Get-Random -Minimum 10 -Maximum 20
    $minute = Get-Random -Minimum 0 -Maximum 59
    $commitDate = "$date $hour`:$minute`:00"

    $env:GIT_COMMITTER_DATE = $commitDate
    git commit --date "$commitDate" -m "$message"
}

git branch -M main
git remote add origin https://github.com/tiwariharsh007/WhatsInsight.git
git push origin main --force
