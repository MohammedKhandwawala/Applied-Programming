Fs = 60; 
% Sampling frequency
t = -.5:1/Fs:.5; 
x = 1/(sqrt(2*pi*0.01))*(exp(-t.^2/(2*0.01)));
nfft = 1024;
% Length of FFT
nfft=1024;
%Length of FFT
% Take fft, padding with zeros so that length(X) is equal to nfft 
X = fftshift(fft(x,nfft)); 

% Take the magnitude of fft of x
mx = abs(X);
% This is an evenly spaced frequency vector
f = (-nfft/2:nfft/2-1)*Fs/nfft; 
% Generate the plot

figure(1);
plot(t,x);
title('Gaussian Pulse Signal'); 
xlabel('Time (s)'); 
ylabel('Amplitude'); 
figure(2);

figure(2);
plot(f,mx); 
title('Power Spectrum of a Gaussian Pulse'); 
xlabel('Frequency (Hz)'); 
ylabel('Power'); 