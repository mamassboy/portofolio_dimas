import 'package:flutter/material.dart';

class UserProvider  extends ChangeNotifier {
  String _Name = "Dimas";
  TextEditingController usernameCtrl = TextEditingController();
  String get dataName => _Name;

  set gantiName(x) {
    _Name = x;
    notifyListeners();
  }

  set namaBaru(x) {
    _Name = x;
    notifyListeners();
  }
} 