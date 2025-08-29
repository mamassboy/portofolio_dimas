import 'package:flutter/material.dart';

class HomeWalletScreen extends StatefulWidget {
  const HomeWalletScreen({super.key});

  @override
  State<HomeWalletScreen> createState() => _HomeWalletScreenState();
}

class _HomeWalletScreenState extends State<HomeWalletScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('latihan m010'),          
      ),

      body: Column(
        children: [
          Text("Welcome Home Dimas")
          

        ],
      ),

    );
  }
}