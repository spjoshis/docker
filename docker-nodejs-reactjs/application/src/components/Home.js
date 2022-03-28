const Home = (props) => {
    return <div className="App">
        <header className="App-header">
            <h1>Hello {props.name}!</h1>
            <p>
                Edit <code>src/App.js</code> and save to reload.
            </p>
        </header>
    </div>;
};

export default Home;