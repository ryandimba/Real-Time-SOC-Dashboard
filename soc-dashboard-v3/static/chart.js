const ctx = document.getElementById('healthChart')

new Chart(ctx,{
type:'line',
data:{
labels:['1am','4am','7am','10am','1pm','4pm','7pm'],
datasets:[{
label:'Network Health',
data:[98,99,97,99,100,99,98]
}]
}
})