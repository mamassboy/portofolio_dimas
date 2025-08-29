import 'package:aplikasi/user_provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final Provider = context.watch<UserProvider>();
    final readProvider = context.read<UserProvider>();
    return Scaffold(
      appBar: AppBar(),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            Text(
              "Welcome dimas",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Text(
                Provider.dataName,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
              ),
            ),

            TextField(
              controller: readProvider.usernameCtrl,
              decoration: InputDecoration(
                labelText: "Username",
                hintText: "masukkan username",
                border: OutlineInputBorder(),
              ),
            ),

            ElevatedButton(
              onPressed: () {
                readProvider.namaBaru = readProvider.usernameCtrl.text;
              },
              child: Text('Change'),
            ),
          ],
        ),
      ),
    );
  }
}
