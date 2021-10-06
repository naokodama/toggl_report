var $window = $(window);
var $year = $('#id_year');
var $month = $('#id_month');
var $tbody = $('#id_calendar_body');
var currentYear;
var currentMonth;

$window.on('load',function(){
    var today = $('#today').text() === "" ? new Date() : new Date($('#today').text());
    currentYear = today.getFullYear();
    currentMonth = today.getMonth();
    calendarHeading(currentYear, currentMonth);
    calendarBody(currentYear, currentMonth, today);
});

function prevMonth() {
    var newDate = addMonth(currentYear, currentMonth, 1, -1);
    currentYear = newDate.getFullYear();
    currentMonth = newDate.getMonth();
    var today = $('#today').text() === "" ? new Date() : new Date($('#today').text());
    calendarHeading(currentYear, currentMonth);
    calendarBody(currentYear, currentMonth, today);
}

function nextMonth() {
    var newDate = addMonth(currentYear, currentMonth, 1, 1);
    currentYear = newDate.getFullYear();
    currentMonth = newDate.getMonth();
    var today = $('#today').text() === "" ? new Date() : new Date($('#today').text());
    calendarHeading(currentYear, currentMonth);
    calendarBody(currentYear, currentMonth, today);
}

$('#prev_month').on('click', function() {
    prevMonth();
});

$('#next_month').on('click', function() {
    nextMonth();
});

function calendarBody(year, month, today){
    var todayYMFlag = today.getFullYear() === year && today.getMonth() === month ? true : false; // 本日の年と月が表示されるカレンダーと同じか判定
    var startDate = new Date(year, month, 1); // その月の最初の日の情報
    var endDate  = new Date(year, month + 1 , 0); // その月の最後の日の情報
    var startDay = startDate.getDay();// その月の最初の日の曜日を取得
    var endDay = endDate.getDate();// その月の最後の日の曜日を取得
    var textSkip = true; // 日にちを埋める用のフラグ
    var textDate = 1; // 日付(これがカウントアップされます)
    var tableBody =''; // テーブルのHTMLを格納する変数

    for (var row = 0; row < 6; row++){
        var tr = '<tr>';

        for (var col = 0; col < 7; col++) {
            if (row === 0 && startDay === col){
                textSkip = false;
            }
            if (textDate > endDay) {
                textSkip = true;
            }
            var addClass = todayYMFlag && textDate === today.getDate() ? 'is-today' : '';
            var textTd = textSkip ? ' ' : textDate++;
            var td = '<td class="'+addClass+'"><a href="'+ generateUrlOfTheDay(year, parseInt(month) + 1, textTd) + '">' + textTd + '</a></td>';
            tr += td;
        }
        tr += '</tr>';
        tableBody += tr;
    }
    $tbody.html(tableBody);
}

function calendarHeading(year, month){
    $year.text(year);
    $month.text(month + 1);
}

function addMonth(year, month, day, moveValOfMonth) {
    while(true) {
        if (month + moveValOfMonth > 11) {
            year += 1;
            month = month + moveValOfMonth - 12;
        } else if (month + moveValOfMonth < 0) {
            year -= 1;
            month = month + moveValOfMonth + 12;
        } else {
            month = month + moveValOfMonth;
        }
        if (month <= 11 && month >= 0) {
            break;
        }
    }
    return new Date(year, month, day);
}

function generateUrlOfTheDay(year, month, day) {
    var urlText;
    var dateStr = year + '-' + month + '-' + day;
    urlText = '../' + dateStr + '/';
    return urlText;
}
