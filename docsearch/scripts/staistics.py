from nltk import FreqDist
from operator import itemgetter


def theFirst20Reccurent(labels, data):
    str = str = """<script>
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: {labels},
                    datasets: [{
                        label: '# of Votes',
                        data: [12, 19, 3, 5, 2, 3],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        </script>"""

    return str


def theFirst20ReccurentTable(data):
    fd = FreqDist(data)
    sortedFD = sorted(fd.items(), key=itemgetter(1), reverse=True)
    for item in sortedFD[:20]:
        print(item, ":", fd[item])
    return str


def searchPopUp(data, data_1):
    str = """<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
            aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body text-right">"""
    str = str + data + """
                    </div>
                    <div class="modal-footer text-right">"""
    str = str + data_1 + """
                    </div>
                </div>
            </div>
        </div>"""

    return str


def validationPopUp():
    str = """<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
            aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body text-right">
                        <h3>تمت عملية اظافة النص</h3>
                    </div>
                </div>
            </div>
        </div>"""
    str = "<script>alert(\"تمت عملية اظافة النص\")</script>"
    return str


def historyAge(data):
    if data == 'acreljahlia':
        str_s = 'العصر الجاهلي'
    elif data == 'acrfjrislam':
        str_s = 'فجر الإسلام'
    elif data == 'acrelhadith':
        str_s = 'العصرالحديث'
    else:
        str_s = 'القرآن'

    return str_s
