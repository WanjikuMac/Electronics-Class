import React, { Component } from 'react';
import { View, Text, StyleSheet, Image} from 'react-native';

export default class Splash extends Component {
    render() {
        return (
            <View style={styles.container}>
                <View style={styles.containerTitle}>
                    <Image
                        style={styles.logo}
                        source={require('../images/calculator.png')}
                    />
                    <Text style={styles.title}>Calculator</Text>
                 </View>
                <Text style={styles.subTitle}>Powered by ReactNative</Text>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center', // center vertically
        alignItems: 'center', //center horizontaly
        backgroundColor: '#27ae60'
    },
    containerTitle: {
        flex: 1,
        justifyContent: 'center', // center vertically
        alignItems: 'center', //center horizontaly
    },
    title: {
        color: 'white',
        fontSize: 35,
        fontWeight: 'bold',
    },
    subTitle: {
        color: 'white',
        fontSize: 15,
        fontWeight: '200',
        paddingBottom: 20
    },
    logoContainer:{
        justifyContent: 'center',
        alignItems: 'center',
    },
    logo: {
        width: 150,
        height: 150
    },
})
