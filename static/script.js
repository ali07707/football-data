// Fonction pour afficher le message d'erreur
function showError(message) {
    var errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger';
    errorDiv.appendChild(document.createTextNode(message));
    var container = document.querySelector('.container');
    var form = document.querySelector('#search-form');
    container.insertBefore(errorDiv, form);
    setTimeout(function() {
        document.querySelector('.alert').remove();
    }, 3000);
}

// Fonction pour afficher les statistiques du joueur
function showStats(playerName, photo) {
    var statsDiv = document.createElement('div');
    statsDiv.className = 'player-stats';
    var img = document.createElement('img');
    img.src = 'data:image/png;base64,' + photo;
    statsDiv.appendChild(img);
    var h3 = document.createElement('h3');
    h3.appendChild(document.createTextNode(playerName));
    statsDiv.appendChild(h3);
    var container = document.querySelector('.container');
    container.appendChild(statsDiv);
}

// Écouteur d'événement pour le formulaire de recherche
document.querySelector('#search-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var playerInput = document.querySelector('#player');
    var playerName = playerInput.value;
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({player: playerName})
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        if (data.error) {
            showError(data.error);
        } else {
            showStats(data.player_name, data.photo);
        }
    })
    .catch(function(error) {
        showError('Une erreur est survenue lors de la recherche du joueur.');
    });
});
