import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, LSTM, Dropout, Flatten, Dense
from .model_utils import one_hot_encode

def data_loader(pos_seqs, neg_seqs):
    labels = [1]*len(pos_seqs) + [0]*len(neg_seqs)
    seqs = pos_seqs + neg_seqs
    X = np.array([one_hot_encode(seq) for seq in seqs])
    return train_test_split(X, labels, test_size=0.2, random_state=42)

def build_conv_lstm_model(input_shape):
    model = Sequential([
        Conv1D(128, 4, activation='relu', input_shape=input_shape),
        MaxPooling1D(2),
        Conv1D(512, 3, activation='relu'),
        MaxPooling1D(2),
        Dropout(0.1),
        LSTM(128, return_sequences=False),
        Dropout(0.2),
        Flatten(),
        Dense(50, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(pos_seqs, neg_seqs, epochs=10, batch_size=64):
    X_train, X_test, y_train, y_test = data_loader(pos_seqs, neg_seqs)
    y_train = np.array(y_train)
    y_test  = np.array(y_test)
    model = build_conv_lstm_model((X_train.shape[1],4))
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test))
    return model
