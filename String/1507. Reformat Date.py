class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
            "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'
        }

        tracker = ['s', 'n', 'r', 't']
        day = ''

        date = date.split(' ')
        if date[0][1] not in tracker:
            day = date[0][0] + date[0][1]
        else:
            day = '0' + date[0][0]

        updated_date = date[-1] + '-' + months[date[-2]] + '-' + day
        return updated_date