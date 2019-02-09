import { React, Component } from 'react';
import './App.css';

class Point extends Component {
  render() {
    return (
      <div className="point">
        <span className='pointText'>{this.props.name}</span>
      </div>
    );
  }
}

class WeatherIcon extends Component {
  render() {
    return (
      <div>
        <span className="weather">{this.props.weather}</span>
        <span className="temp">{this.props.temp}</span>
      </div>
    );
  }
}

class Popup extends Component {
  render() {
    return (
      <div>
        <WeatherIcon weather="moi" temp="moimoi"/>
      </div>
    );
  }
}



class Test extends Component {
  render() {
    return (
      <div>
        <div className="header">
          <h1>Naturoutes></h1>
        </div>
        <div>
          <Point name="moi"/>
        </div>
      </div>
    );
  }
}

export default Test;
