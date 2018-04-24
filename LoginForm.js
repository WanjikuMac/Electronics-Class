import React, { Component } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';

export default class LoginForm extends Component {
	render(){
		return(
			<View style={styles.container}>
			<TextInput style={styles.input}
					placeholder = 'Enter Username or Email'
					placeholderTextColor ='rgba(255,255,255,0.)'
			/>
			<TextInput style={styles.input}
					placeholder = 'Enter Password'
					placeholderTextColor ='rgba(255,255,255,0.)'
					SecureTextEntry
			/>
			<TouchableOpacity style={styles.buttonContainer}>
				<Text style={styles.buttonStyle}> Log In</Text>
			</TouchableOpacity>
			</View>
		)
	}
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  input: {
  	height:40,
  	marginBottom: 10,
  	color: 'white',
  	paddingHorizontal: 10,
  	backgroundColor:'rgba(255,255,255,0.2)'
  },
  buttonContainer:{
  	backgroundColor:'#2980b9',
  	PaddingVertical: 15,
  },
  buttonStyle:{
  	color:'white',
  	fontSize: 12,
  	fontWeight:'bold',
  	textAlign:'center',
  },
})