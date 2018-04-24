import React, { Component } from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';

import LoginForm from './LoginForm';

export default class Login extends Component {
  render(){
    return(
        /* Main Container */
      <View style={styles.container}>
        <View style={styles.logoContainer}>
            <Image
                style={styles.logo}
                source={require('../images/calculator.png')}
            />
            <Text style={styles.titleText}>Calculator</Text>
        </View>
        <View style={styles.formContainer}>
            <LoginForm/>
     </View>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#3498db'
  },
  logoContainer: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  logo: {
    width: 100,
    height: 100
  },
  titleText: {
    fontWeight: 'bold',
    color: 'white',
    fontSize: 45,
    textAlign: 'center',
    opacity: 0.8,
  },
  formContainer:{
    padding:20,
  }
})
