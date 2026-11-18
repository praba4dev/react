
import React, { useState } from 'react';

import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Platform,
  Alert
} from 'react-native';

export default function LoginScreen({ navigation }) {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Alert function for Web and Mobile
  const showMessage = (title, message) => {

    if (Platform.OS === 'web') {
      window.alert(title + '\n\n' + message);
    } else {
      Alert.alert(title, message);
    }

  };

  // Login validation
  const handleLogin = () => {

    if (email === '' || password === '') {

      showMessage('Error', 'Please enter email and password');

    }

    else if (
      email === 'john@gmail.com' &&
      password === '123456'
    ) {

      showMessage('Success', 'Login successful');

    }

    else {

      showMessage('Login Failed', 'Invalid email or password');

    }

  };

  return (

    <View style={styles.container}>

      <View style={styles.logo}>
        <Text>Book Nest</Text>
      </View>

      <Text style={styles.heading}>
        Welcome Back
      </Text>

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />

      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry={true}
      />

      <TouchableOpacity
        style={styles.button}
        onPress={handleLogin}
      >
        <Text style={styles.buttonText}>
          Login
        </Text>
      </TouchableOpacity>

      <TouchableOpacity
        onPress={() => navigation.navigate('Register')}
      >
        <Text style={styles.link}>
          Don't have an account? Register
        </Text>
      </TouchableOpacity>

    </View>

  );

}

const styles = StyleSheet.create({

  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    paddingTop: 50,
    paddingHorizontal: 20,
    backgroundColor: '#FFFFFF',
  },

  logo: {
    width: 150,
    height: 150,
    backgroundColor: '#DDDDDD',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
    borderRadius: 8,
  },

  heading: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 25,
    color: '#000000',
  },

  input: {
    width: 300,
    height: 45,
    borderWidth: 1,
    borderColor: '#CCCCCC',
    borderRadius: 8,
    paddingHorizontal: 10,
    fontSize: 16,
    marginBottom: 15,
  },

  button: {
    width: 300,
    height: 45,
    backgroundColor: '#1E5AA8',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
  },

  buttonText: {
    color: '#FFFFFF',
    fontSize: 20,
  },

  link: {
    fontSize: 16,
    color: '#1E5AA8',
  },

});
