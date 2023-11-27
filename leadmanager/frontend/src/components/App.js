import React from "react";
import ReactDOM from "react-dom";
import Heros from "./layout/heros";

class App extends React.Component {
  render() {
    return (
      <div>
        
       <Heros/>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
