function gera_cor(qtd=2){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }

    return [bg_color, border_color];

}



function total_renda(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_renda').innerHTML = data.total
    })
}
console.log('Deus é o meu Fiel Amigo!')

function total_contas(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_dividas').innerHTML = data.total
    })
}
console.log('Deus é o meu Fiel Amigo!')


function total_invest(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_invest').innerHTML = data.total
    })
}
console.log('Deus é o meu Fiel Amigo!')


function renderiza_despesas(url){
    fetch(url, {
        method:'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('despesas').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.labels,
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[1],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 0
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    })
}

function renderiza_renda(url){
    fetch(url, {
        method:'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('rendas').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.labels,
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[1],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 0
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    })
}


function renderiza_investimento(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('invest').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.labels,
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[1],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                        reverse: true,

                        labels: {
                            font: {
                                weight: 'bold'
                            }
                        },
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true

                    }
                }
            }
        });


    })
}



