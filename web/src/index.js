let api_url = 'http://34.76.189.193/api'
// const api_url = 'http://10.132.0.8/api'
// const api_url = 'http://localhost:5000/api'

async function get_movie_url (movie_name) {
    let response = await(fetch(api_url + '/db/get_film_link/' + movie_name));
    let data = await response.json();
    return data;
}

async function change_video_url(movie_name) {
    console.log("in func");
    video = document.getElementById('video');
    console.log("video is "+ video);


    let vurlj = await get_movie_url(movie_name);
    let vurl = vurlj.url;
    source = document.createElement('source');
    source.setAttribute("src", vurl);
    source.setAttribute("type", "video/mp4");
    video.appendChild(source);
}
console.log("in js file");
window.onload = async () => { await change_video_url("movie1")};