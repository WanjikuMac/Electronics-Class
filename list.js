import React, { Component } from 'react';
import { View, StyleSheet, Image, TouchableOpacity, Text} from 'react-native';


export default class list extends Component{
	state={
		lessons:[
		{ 
			id: 0,
			name: 'Graphic Design',
		},

		{ 
			id: 1,
			name: 'Python',
		},

		{ 
			id: 2,
			name: 'CSS',
		},

		{ 
			id: 3,
			name: 'Mobile Application',
		},

		{ 
			id: 4,
			name: 'c++',
		},

		]
	}
	alertItem = (item) => {
		alert(item.name)
	}
	render(){
		return(
		<view style=(styles.container)>
		{
			this.state.lessons.map((item, index )=>(
				<TouchableOpacity key={item.id}
				onPress ={() => this.alertItem(item)}>

				<Text style = styles.text>
				{item.name}
				</Text>

				<view style=(styles.separator)>
				
				</TouchableOpacity>

				</View>

				)
			
		}
		</view>
	)}
}
const styles =StyleSheet.create({
	container:
	{
		flex:1,
		padding:10,
		backgroundColor:'#2ecc71',
		alignItems: 'center'

	};
	text:{
		color:'white',
		fontSize:20
	};
	separator:
	{
		height:0.5,
		width: 100%;
		backgroundColor:'white',
		padding: 3
	}
})