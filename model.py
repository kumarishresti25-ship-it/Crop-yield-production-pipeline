import numpy as np
from sklearn.ensemble import RandomForestRegressor

def build_cnn_feature_extractor():
    """3D-CNN to extract features from satellite image stacks."""
    model = tf.keras.Sequential([
        tf.keras.layers.Conv3D(32, (3, 3, 3), activation='relu', input_shape=(64, 64, 5, 4)),
        tf.keras.layers.MaxPooling3D((2, 2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu')
    ])
    return model

# We train the RF on the combined features
def train_hybrid_model(cnn_features, weather_data, targets):
    combined_features = np.hstack([cnn_features, weather_data])
    rf = RandomForestRegressor(n_estimators=100)
    rf.fit(combined_features, targets)
    return rf