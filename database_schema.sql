-- Database Schema for Campus Assignment Management System

-- Create Database
CREATE DATABASE IF NOT EXISTS campus_api;
USE campus_api;

-- 1. Student Table (Custom User Model)
CREATE TABLE IF NOT EXISTS api_student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME(6),
    is_superuser TINYINT(1) NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    is_staff TINYINT(1) NOT NULL,
    is_active TINYINT(1) NOT NULL,
    date_joined DATETIME(6) NOT NULL,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    year INT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    username VARCHAR(150) NULL UNIQUE
);

-- 2. Assignment Table
CREATE TABLE IF NOT EXISTS api_assignment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at DATETIME(6) NOT NULL,
    student_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES api_student(id) ON DELETE CASCADE
);
