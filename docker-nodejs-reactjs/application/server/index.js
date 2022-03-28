import path from 'path';
import fs from 'fs';

import React from 'react';
import ReactDOMServer from 'react-dom/server';
import express from 'express';

import App from '../src/App';
import Users from '../src/components/Users';

const PORT = process.env.PORT || 3006;
const app = express();


const render = (res, component) => {
    const indexFile = path.resolve('./build/index.html');
    const app = ReactDOMServer.renderToString( component );
    fs.readFile(indexFile, 'utf8', (err, data) => {
        if (err) {
            console.error('Something went wrong:', err);
            return res.status(500).send('Oops, better luck next time!');
        }

        return res.send(
            data.replace('<div id="root"></div>', `<div id="root">${app}</div>`)
        );
    });
}

app.get('/', (req, res) => {
    return render(res, <App />);
});

app.use(express.static('./build'));

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});