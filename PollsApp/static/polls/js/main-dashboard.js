function _map_polls(array){
    const pollsDate = {};
    let date, formatedDate;
    Array.from(array).forEach(e => {
        date = new Date(e.date_created);
        formatedDate = `${date.getUTCDate()}/${date.getUTCMonth()+1}/${date.getUTCFullYear()}`;
        formatedDate in pollsDate ? pollsDate[formatedDate] += 1 : pollsDate[formatedDate] = 1;
    });

    return pollsDate;
}

function _map_users(array) {
    const usersYear = {};
    let date, year;
    Array.from(array).forEach(e => {
        date = new Date(e.date_joined);
        year = date.getUTCFullYear();
        year in usersYear ? usersYear[year] += 1 : usersYear[year] = 1;
    });

    return usersYear;
}

function buildPollChart(url) {
    fetch(url)
        .then(res => res.json())
        .then(data => {
            const pollsData =  _map_polls(data);
            const labelsPolls = Object.keys(pollsData).sort((a,b) => {
                if(a > b) return 1;
                else if(b > a) return -1;
                return 0;
            });

            new Chart($('#polls-chart').get(0), {
                type: 'line',
                data: {
                    labels: labelsPolls,
                    datasets: [{
                        label: 'Polls Created',
                        data: labelsPolls.map(lbl => pollsData[lbl]),
                        tension: 0.05,
                        borderColor: '#00FB94',
                        backgroundColor: '#98FFD5'
                    }],
                },
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Polls Created'
                        }
                    },
                    responsive: true,
                }
            });
        })
        .catch(console.error)
}

function buildUsersChart(url) {
    fetch(url)
        .then(res => res.json())
        .then(data => {
            const usersData =  _map_users(data);
            const yearsLabels = Object.keys(usersData).sort();

            new Chart($('#users-chart').get(0), {
                type: 'line',
                data: {
                    labels: yearsLabels,
                    datasets: [{
                        label: 'Users Registered',
                        data: yearsLabels.map(lbl => usersData[lbl]),
                        tension: 0.05,
                    }],
                },
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Users Registered by Year'
                        }
                    },
                    responsive: true,
                }
            });
        })
        .catch(console.error)
}