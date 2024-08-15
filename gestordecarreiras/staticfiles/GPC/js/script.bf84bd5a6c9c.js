$(document).ready(function () {
    $('#id_cep').on('blur', function () {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep.length != 8) {
            return;
        }
        $.getJSON('https://viacep.com.br/ws/' + cep + '/json/', function (data) {
            if (!('erro' in data)) {
                $('#id_endereco').val(data.logradouro);
                $('#id_bairro').val(data.bairro);
                $('#id_cidade').val(data.localidade);
                $('#id_estado').val(data.uf);
            } else {
                alert('CEP não encontrado.');
            }
        });
    });
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Rola a página para o topo suavemente
}
function showStep(step) {
    var steps = document.getElementsByClassName("step");
    for (var i = 0; i < steps.length; i++) {
        steps[i].style.display = "none";
    }
    steps[step].style.display = "block";

    // atualizacao da barra de progresso
    // var progress = Math.round(step / (steps.length - 1) * 100); 
    // var progressBar = document.querySelector(".progress-bar");
    // progressBar.style.width = progress + "%";
    // progressBar.setAttribute("aria-valuenow", progress);

    scrollToTop();
}

function nextStep(currentStep) {
    if (validateStep(currentStep)) {
        showStep(currentStep + 1);
    }
}

function prevStep(currentStep) {
    showStep(currentStep - 1);
}

function validateStep(step) {
    // Aqui você pode adicionar lógica de validação do formulário se necessário
    return true; // Retorne true se a validação passar, false caso contrário
}

document.addEventListener("DOMContentLoaded", function () {
    var steps = document.getElementsByClassName("step");
    showStep(0); // Mostra a primeira etapa inicialmente

    var nextBtns = document.getElementsByClassName("nextBtn");
    var prevBtns = document.getElementsByClassName("prevBtn");

    // Adiciona listeners para os botões Próximo e Anterior
    for (var i = 0; i < nextBtns.length; i++) {
        nextBtns[i].addEventListener("click", function () {
            var currentStep = parseInt(this.getAttribute("onclick").match(/\d+/)[0]);
            nextStep(currentStep);
        });
    }

    for (var i = 0; i < prevBtns.length; i++) {
        prevBtns[i].addEventListener("click", function () {
            var currentStep = parseInt(this.getAttribute("onclick").match(/\d+/)[0]);
            prevStep(currentStep);
        });
    }

});


// formularios simples (perfis)
$(document).ready(function () {
    $('#cep').on('blur', function () {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep.length != 8) {
            return;
        }
        $.getJSON('https://viacep.com.br/ws/' + cep + '/json/', function (data) {
            if (!('erro' in data)) {
                $('#endereco').val(data.logradouro);
                $('#bairro').val(data.bairro);
                $('#cidade').val(data.localidade);
                $('#estado').val(data.uf);
            } else {
                alert('CEP não encontrado.');
            }
        });
    });
});

function showEndereco() {
    var endereco = document.getElementsByClassName("campos-de-endereco")[0];
    if (endereco.style.display === "none" || endereco.style.display === "") {
        endereco.style.display = "block";
    } else {
        endereco.style.display = "none";
    }
}